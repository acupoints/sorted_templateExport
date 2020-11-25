
if __name__ == "__main__":
    import os
    import shutil
    import re
    from TextfileIO import TextfileIO
    ##
    tio = TextfileIO()
    dirs = "output"
    if not os.path.exists(dirs):
        os.makedirs(dirs)
        print("--> Created directory [{}]".format(dirs))

    ini_contents = tio.read("plnsrv.ini")
    all_lines = []
    temp_list = []
    segment_name = "--"
    segments = [segment_name]
    segment_dict = {}

    for ini_contents_el in ini_contents:
        
        # print("--> {}".format(ini_contents_el))
        matched = re.findall(r"\[(.+?)\]", ini_contents_el)
        if len(matched)>0:
            # print("--> {}".format(matched))
            segment_name = matched[0]
            segments.append(segment_name)
        else:
            if ini_contents_el.strip()!="":
                if segment_name in segment_dict:
                    segment_dict[segment_name].append(ini_contents_el)
                else:
                    segment_dict[segment_name]=[ini_contents_el]
        
    # print(segment_dict.keys())
    # print(segments)
    ##
    all_lines = []
    segments_sorted = sorted(segment_dict['brand name'])
    segment_dict['brand name'] = segments_sorted
    for segments_el in segments:
        # if segments_el=='brand name':
        #     segment_dict[segments_el]=sorted(segment_dict[segments_el])
        if segments_el!='--':
            all_lines.append("[{}]".format(segments_el))
        all_lines.append("\n".join(segment_dict[segments_el]))
        all_lines.append("\n")
    tio.write("output\\plnsrv.ini", all_lines)
    print("--> {}".format("Output sorted target configuration file"))
    ###
    html_tr_list = []
    for segments_sorted_el in segments_sorted:
        html_tr_list.append("\t\t<tr><td>{machine_type}</td><td>{eeprom_string}</td></tr>".format(
            machine_type=segments_sorted_el.split("=")[0],
            eeprom_string=segments_sorted_el.split("=")[1]
        ))
    html_contents = tio.read("eeprom.html")
    html_contents_new = []
    continued = True
    for html_contents_el in html_contents:
        if len(re.findall(r"<!--placeholder-begin-->", html_contents_el))>0:
            continued = False
            html_contents_new.append("\n".join(html_tr_list)) 
        if len(re.findall(r"<!--placeholder-end-->", html_contents_el))>0:
            continued = True
        if not continued:
            continue

        html_contents_new.append(html_contents_el)
    tio.write("output\\eeprom.html", html_contents_new)
    print("--> {}".format("Output sorted target page file"))
    print("-"*32)
    print("--> {}".format("All operations completed"))
    # pass

    