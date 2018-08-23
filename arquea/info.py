class InfoArquea:

    def __init__(self):
        self.version = 0.1
        self.name = "ArqueaDB"
        self.release_date = "ArqueaDB v{} 2018-08-22".format(self.version)
        self.repository = "https://github.com/gabriellasaro/"
        # self.compatible_version = (0.1,)
    
    def get_info(self):
        return (self.version, self.name, self.release_date, self.repository)
    
    def get_name(self):
        return self.name
    
    def get_version(self):
        return self.version
    
    def get_release(self):
        return self.release_date
    
    def get_repository(self):
        return self.repository