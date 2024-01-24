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
    file = open("firstpage_175_no_col.csv","r")
    
    f = file.readlines()
    file.close()
    my_district = f[distric_index].split(",")
    selected_index = []
    selected = []
    # 1.372 -0.0204 0.6866 0.9105

    for i in range(len(my_district)):
        try:
            if float(my_district[i])<= mark:
                selected_index.append(i)
                
        except:
            
            pass   
    
    for i in selected_index:
        selected.append(data_list[i])
        
        pass
    print(len(data_list))
    print(len(my_district))
   
    
    return (selected)             


# zScore("RATNAPURA",1.372)

def subs(s1,s2,s3):

    subjects_all = {
    "COMBINED MATHEMATICS",
    "BUDDHISM",
    "HINDUISM",
    "CHRISTIANITY",
    "ISLAM",
    "BUDDHIST CIVILIZATION",
    "HINDU CIVILIZATION",
    "ISLAMIC CIVILIZATION",
    "CHRISTIAN CIVILIZATION",
    "BIOLOGY",
    "ECONOMICS",
    "ART",
    "DANCING (INDIGENOUS)",
    "DANCING (BHARATHA)",
    "ORIENTAL MUSIC",
    "CARNATIC MUSIC",
    "WESTERN MUSIC",
    "LOGIC & SCIENTIFIC METHOD",
    "ENGINEERING TECHNOLOGY",
    "BIO SYSTEMS TECHNOLOGY",
    "BUSINESS STUDIES",
    "AGRICULTURAL SCIENCE",
    "GERMAN",
    "PHYSICS",
    "PALI",
    "SINHALA",
    "TAMIL",
    "CIVIL TECHNOLOGY",
    "MECHANICAL TECHNOLOGY",
    "ELECTRICAL, ELECTRONIC AND INFORMATION TECHNOLOGY",
    "FOOD TECHNOLOGY",
    "AGRO TECHNOLOGY",
    "BIO RESOURCE TECHNOLOGY",
    "BUSINESS STATISTICS",
    "SANSKRIT",
    "CHEMISTRY",
    "SCIENCE FOR TECHNOLOGY",
    "DRAMA & THEATRE (SINAHALA)",
    "DRAMA & THEATRE (TAMIL)",
    "DRAMA & THEATRE (ENGLISH)",
    "POLITICAL SCIENCE",
    "FRENCH",
    "ENGLISH",
    "HOME ECONOMICS",
    "ACCOUNTING",
    "HISTORY OF INDIA",
    "HISTORY OF EUROPE",
    "HISTORY OF MODERN WORLD",
    "ARABIC",
    "MALAY",
    "CHINESE",
    "INFORMATION & COMMUNICATION TECHNOLOGY",
    "HISTORY OF SRI LANKA",
    "HINDI",
    "KOREAN",
    "MATHEMATICS",
    "HIGHER MATHEMATICS",
    "RUSSIAN",
    "GREEK AND ROMAN CIVILIZATION",
    "JAPANESE",
    "GEOGRAPHY",
    "COMMUNICATION & MEDIA STUDIES"
}
    file_subject_req = open("test")
    k = file_subject_req.readlines()
    cap_subjects = []
    for i in range(len(k)):
        one_line_sub = k[i].split("||")[1].split(",")
  
        for p in range(len(one_line_sub)):
            one_line_sub[p] = one_line_sub[p].strip()
        
        if (s1 in one_line_sub) and (s2 in one_line_sub) and (s3 in one_line_sub):
            cap_subjects.append(k[i].split("||")[0])
            
        

    print(cap_subjects)
        
ss1 = "COMBINED MATHEMATICS"
ss2 = "BUDDHISM"
ss3 = "SCIENCE FOR TECHNOLOGY"

subs(ss1,ss2,ss3)


