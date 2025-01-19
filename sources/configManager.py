import configparser
import os
import sys

class ConfigManager:
    def __init__(self, file_name="config.ini"):
        self.file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
        self.config = configparser.ConfigParser()

        if not os.path.exists(self.file_path):
            print(f"⚠️  Конфигурационный файл '{self.file_path}' не найден. Работа прервана.")
            sys.exit(1)

        self.load_config()
        self.validate_config()

    def load_config(self):
        self.config.read(self.file_path)

    def validate_config(self):
            required_sections = {
                "settings": ["path2inbox", "path2result"],
            }
            error_flag = False
            for section, keys in required_sections.items():
                if not self.config.has_section(section):
                    print(f"❌ Ошибка: Отсутствует секция [{section}] en '{self.file_path}'.")
                    sys.exit(1)

                for key in keys:
                    if not self.config.has_option(section, key):
                        error_flag = True
                        print(f"❌ Ошибка: Отсутствует настройка '{key}' в секции [{section}] в '{self.file_path}'.")
            if error_flag:
                print(f"⚠️  Конфигурационный файл '{self.file_path}' содержит ошибки. Работа прервана.")
                sys.exit(1)

            # # Verificar tipos de datos
            # try:
            #     self.config.getboolean("general", "debug")
            #     self.config.getint("general", "timeout")
            #     self.config.getint("database", "port")
            # except ValueError as e:
            #     print(f"❌ ERROR: Tipo de dato incorrecto en la configuración: {e}")
            #     sys.exit(1)

            print("✅ Проверка конфигурации прошла успешно.")
    
    def get_path2inbox(self):
        return self.config.get("settings", "path2inbox")
    
    def get_path2result(self):
        return self.config.get("settings", "path2result")
