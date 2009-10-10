import difflib

def write_blob_diff(f, (old_path, old_mode, old_blob), 
                       (new_path, new_mode, new_blob)):
    :param (old_path, old_mode, old_blob): Previous file (None if nonexisting)
    :param (new_path, new_mode, new_blob): New file (None if nonexisting)
    def blob_id(blob):
        if blob is None:
            return "0" * 7
        else:
            return blob.id[:7]
    def lines(blob):
        if blob is not None:
            return blob.data.splitlines(True)
        else:
            return []
    f.write("index %s..%s %o\n" % (
        blob_id(old_blob), blob_id(new_blob), new_mode))
    old_contents = lines(old_blob)
    new_contents = lines(new_blob)
    f.writelines(difflib.unified_diff(old_contents, new_contents, 
        old_path, new_path))