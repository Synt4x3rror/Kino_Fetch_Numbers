import os

class FileHelper:
    @staticmethod
    def load_yaml(path_to_yaml):
        import yaml
        try:
            if not os.path.isfile(path_to_yaml):
                raise FileNotFoundError(f'File at "{path_to_yaml}" not found')
            file = open(path_to_yaml, 'r')
            content = yaml.load(file, yaml.FullLoader)
            file.close()

            return content

        except Exception as e:
            print('An error has occurred while attempting to load the specified yaml file')
            print(repr(e))
            return None