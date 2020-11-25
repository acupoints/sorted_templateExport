class TextfileIO():
    def print_TextfileIO(self):
        print("--> print_TextfileIO")

    def read(self, source_file, encoding="utf-8"):
        import os
        data = []
        if os.path.exists(source_file):
            with open(source_file, 'r', encoding=encoding) as f:
                data = f.read().splitlines()
            
        return data

    def write(self, target_file, contents, encoding="utf-8"):
        with open(target_file, 'w', encoding=encoding) as f:
            f.writelines(["{}\n".format(contents_el) for contents_el in contents])

    def append(self, target_file, more_contents, encoding="utf-8"):
        contents = self.read(target_file, encoding=encoding)
        contents.extend(more_contents)
        self.write(target_file, contents, encoding=encoding)

    def get_json_dict(self, source_file, encoding="utf-8"):
        import json
        import os
        contents = {}
        if os.path.exists(source_file):
            with open(source_file, 'r', encoding=encoding) as f:
                contents = json.load(f)
        return contents

    def set_json_dict(self, target_file, contents, encoding="utf-8"):
        import json
        with open(target_file, 'w', encoding=encoding) as f:
            json.dump(contents, f, indent=4)
    
    def get_hexdigest(self, plain_text="", hashlib_type="sha256"):
        import hashlib
        if hashlib_type.lower()=="sha1":
            hash_obj = hashlib.sha1()
        elif hashlib_type.lower()=="sha256":
            hash_obj = hashlib.sha256()
        elif hashlib_type.lower()=="sha512":
            hash_obj = hashlib.sha512()
        elif hashlib_type.lower()=="md5":
            hash_obj = hashlib.md5()
        else:
            hash_obj = hashlib.sha256()
        
        hash_obj.update(plain_text.encode('utf-8'))
        encrypts = hash_obj.hexdigest()
        
        return encrypts
    
    def getSHA1(self, fineName, block_size=64 * 1024):
        import hashlib
        import base64
        with open(fineName, 'rb') as f:
            sha1 = hashlib.sha1()
            while True:
                data = f.read(block_size)
                if not data:
                    break
                sha1.update(data)
            rets = base64.b64encode(sha1.digest())
            rets=str(rets,'utf-8')
            return rets
    def getMD5(self, fineName, block_size=64 * 1024):
        import hashlib
        import base64
        with open(fineName, 'rb') as f:
            md5 = hashlib.md5()
            while True:
                data = f.read(block_size)
                if not data:
                    break
                md5.update(data)
            rets = base64.b64encode(md5.digest())
            rets=str(rets,'utf-8')
            return rets
    def zlshell(self, command, print_msg=True):
        import os
        sh_rets = os.popen(command)
        lines = sh_rets.readlines()

        valid_lines = []
        for lines_el in lines:
            el = lines_el.strip()
            if el:
                valid_lines.append(el)
                if print_msg:
                    print("-->{}--".format(el))
        return valid_lines


if __name__ == "__main__":
    tio = TextfileIO()
    # tio.print_TextfileIO()
    source_file = "sample-sha256sum.txt"
    target_file = "sample-sha256sum_temp.txt"
    rets=tio.read(source_file)
    print("{}".format(rets))
    tio.write(target_file, rets)

    pass