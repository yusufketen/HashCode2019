# HashTepe HashCode 2019
from sys import argv as arg


def number_of_common_tags(tags1, tags2):
    return len([tag for tag in tags1 if tag in tags2])


def difference(tags1, tags2):
    return len(tags1)-number_of_common_tags(tags1, tags2)


def interest_factor(tags1, tags2):
    return min(difference(tags1, tags2), difference(tags2, tags1), number_of_common_tags(tags1, tags2))


def get_photo_list(photo_list_str):
    photos = []
    i = 0
    for photo_str in photo_list_str:
        try:
            if(photo_str != ""):
                # photos = list of input(line by line)
                photo = [i]
                photo.extend(photo_str.split(" "))
                photos.append(photo)
                i+=1
        except:
            pass 
    return photos


def tags(photo):
    return photo[3:]


def get_pair_list(lst):
    pair_set = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j:
                curr_pair_set = set([i, j])
                if curr_pair_set not in pair_set:
                    pair_set.append(curr_pair_set)
    return [list(s) for s in pair_set]


def main():
    inputfile = open(arg[1], "r")
    number_of_photos = inputfile.readline()
    photos = get_photo_list(inputfile.read().split("\n"))
    inputfile.close()

    v_photos = [photo for photo in photos if photo[1] == "V"]
    h_photos = [photo for photo in photos if photo[1] == "H"]

    combined_v_photos_temp = []
    v_pair_list = get_pair_list(v_photos)

    for i in range(len(v_pair_list)):
        minimum = v_pair_list[0]
        for pair in v_pair_list:
            vp1 = v_photos[pair[0]]
            vp2 = v_photos[pair[1]]
            if number_of_common_tags(tags(vp1), tags(vp2)) < number_of_common_tags(tags(v_photos[minimum[0]]), tags(v_photos[minimum[1]])):
                minimum = pair
        combined_v_photos_temp.append(
            [v_photos[minimum[0]], v_photos[minimum[1]]])
        v_pair_list.remove(minimum)

    combined_v_photos = []
    for v_photo_pair in combined_v_photos_temp:
        v_photo1 = v_photo_pair[0]
        v_photo2 = v_photo_pair[1]

        combined = [v_photo1[0]]
        combined.append(str(len(tags(v_photo1)) + len(tags(v_photo2)) -
                            number_of_common_tags(tags(v_photo1), tags(v_photo2))))
        combined.extend(list(set(tags(v_photo1) + tags(v_photo2))))
        combined_v_photos.append(combined)

    all_photos = h_photos + combined_v_photos

    sorted_photos = [all_photos[0]]

    for photo1 in all_photos:
        for photo2 in all_photos:
            if interest_factor(tags(sorted_photos[-1]), tags(photo1)) > interest_factor(tags(photo1), tags(photo2)):
                if photo1 not in sorted_photos:
                    sorted_photos.append(photo1)

    print(sorted_photos)
 
   #pair_list = get_pair_list(all_photos)
   #print(pair_list)
   #



   #for i in range(len(pair_list)):
   #    pass
    
    

main()
