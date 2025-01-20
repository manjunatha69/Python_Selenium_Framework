import configparser
import os


class ConfigReader():
    def __init__(self,config_path="config/config.ini"):
        #print(f"Using config file at: {config_path}")
        self.config=configparser.ConfigParser()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_dir, "../config/config.ini")
        self.config.read(config_path)

    def get_app_url(self):
        return self.config.get('app','base_url')

    def get_browser(self):
        return self.config.get('app','browser')

    def get_implicit_wait(self):
        return self.config.get('timeout','implicit_wait')

    def get_page_load(self):
        return self.config.get('timeout', 'page_load_timeout')

    def get_script_time(self):
        return self.config.get('timeout', 'script_timeout')

    def get_timeout(self):
        data={
            'implicit_wait':self.config.getint('timeout','implicit_wait'),
            'page_load_timeout':self.config.getint('timeout','page_load_timeout'),
            'script_timeout':self.config.getint('timeout','script_timeout')
        }
        return  data