def zScore(districs,mark):
    locations = [
    'COLOMBO', 'GAMPAHA', 'KALUTARA', 'MATALE', 'KANDY', 'NUWARA ELIYA',
    'GALLE', 'MATARA', 'HAMBANTOTA', 'JAFFNA', 'KILINOCHCHI', 'MANNAR',
    'MULLAITIVU', 'VAVUNIYA', 'TRINCOMALEE', 'BATTICALOA', 'AMPARA',
    'PUTTALAM', 'KURUNEGALA', 'ANURADHAPURA', 'POLONNARUWA', 'BADULLA',
    'MONARAGALA', 'KEGALLE', 'RATNAPURA'
    ]
    
    data_list = [
    "INFORMATION COMMUNICATION TECHNOLOGY  ||  University of Vavuniya Sri Lanka",
    "INFORMATION COMMUNICATION TECHNOLOGY  ||  Uva Wellassa University of Sri Lanka",
    "PHYSICAL SCIENCE -ICT  ||  University of Sri Jayewardenepura",
    "PHYSICAL SCIENCE -ICT  ||  University of Kelaniya",
    "TRANSLATION STUDIES  ||  University of Kelaniya",
    "TRANSLATION STUDIES  ||  Sabaragamuwa University of Sri Lanka",
    "TRANSLATION STUDIES  ||  University of Jaffna",
    "TRANSLATION STUDIES  ||  Eastern University Sri Lanka",
    "FILM & TELEVISION STUDIES  ||  University of Kelaniya",
    "PROJECT MANAGEMENT  ||  University of Vavuniya Sri Lanka",
    "TEACHING ENGLISH AS A SECOND LANGUAGE (TESL)  ||  University of Sri Jayewardenepura",
    "TEACHING ENGLISH AS A SECOND LANGUAGE (TESL)  ||  University of Kelaniya",
    "VISUAL ARTS  ||  University of the Visual & Performing Arts",
    "MUSIC  ||  University of the Visual & Performing Arts",
    "DANCE  ||  University of the Visual & Performing Arts",
    "DRAMA & THEATRE  ||  University of the Visual & Performing Arts",
    "ART & DESIGN  ||  Ramanathan Academy of Fine Arts",
    "MUSIC  ||  Ramanathan Academy of Fine Arts",
    "DANCE  ||  Ramanathan Academy of Fine Arts",
    "VISUAL & TECHNOLOGICAL ARTS  ||  Swami Vipulananda Institute of Aesthetic Studies",
    "MUSIC  ||  Swami Vipulananda Institute of Aesthetic Studies",
    "DANCE  ||  Swami Vipulananda Institute of Aesthetic Studies",
    "DRAMA & THEATRE  ||  Swami Vipulananda Institute of Aesthetic Studies",
    "FOOD BUSINESS MANAGEMENT [Commerce Stream]  ||  Sabaragamuwa University of Sri Lanka"
]
    distric_index = locations.index(districs)
    f = open("firstpage_175_no_col.csv","r").readlines()
    my_district = f[distric_index].split(",")
    selected_index = []
    selected = []
    # 1.372 -0.0204 0.6866 0.9105

    for i in range(len(my_district)):
        try:
            if float(my_district[i])<= mark:
                selected_index.append(i)
                # print(my_district[i])
        except:
            # print("cant "+str(i))     
            pass   
    
    for i in selected_index:
        selected.append(data_list[i])
    return (selected)             


zScore("RATNAPURA",-0.3596)