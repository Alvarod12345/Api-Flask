class config:
    pass

class developmentConfig(config):
    DEBUG = True

config= {
    'development' : developmentConfig
}