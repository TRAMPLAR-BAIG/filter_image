import os
import hashlib
import datetime

#   @GCT
#   @PrinceMughal_
#   @LinuxPython
#   Date[DD-MM-YY] 23-04-20
#   Time 01:44am THUR


class ImageHashHandler:
    """
        Handler Image Hash maker
    """
    def __init__(self, path_to_image, extension):
        self.__image_hash = list()
        self._load_all_image(path_to_image, extension)

    def _load_all_image(self, path_to_image, extension):
        images = os.listdir(path_to_image)
        for image in images:
            full_path = os.path.join(path_to_image, image)
            if os.path.isfile(full_path) and full_path.endswith(extension):
                self.__image_hash.append(ImageHashHandler.ImageHash(image_title=full_path))

    def get_all_hash(self):
        for image in self.__image_hash:
            image.set_image_hash(self._make_hash(image.get_image_title()))

    def _make_hash(self, file_path):
        file_size = os.stat(file_path).st_size
        hash_file = None
        with open(file_path, 'rb') as file_handler:
            content = file_handler.read(file_size)
            hash_file = hashlib.sha256(content).hexdigest()
        return hash_file

    def print_all(self):
        for image_hash in self.__image_hash:
            print(image_hash)

    class ImageHash:
        """
            Hold Image Title, Hash, When Hash was made
        """
        def __init__(self, image_title, image_hash=None):
            self.__image_title = image_title
            self.__image_hash = image_hash
            self.__image_hash_date = None

        def set_image_title(self, image_title):
            self.__image_title = image_title

        def set_image_hash(self, image_hash):
            self.__image_hash = image_hash
            self.__image_hash_date = datetime.datetime.now()

        def get_image_title(self):
            return self.__image_title

        def get_image_hash(self):
            return self.__image_hash

        def get_hash_timestamp(self):
            return self.__image_hash_date

        def __str__(self):
            return "[When: {}] {} -> {}".format(self.__image_hash_date, os.path.basename(self.__image_title), self.__image_hash)
