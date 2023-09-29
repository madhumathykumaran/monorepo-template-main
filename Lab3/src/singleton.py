class Logger:
    _instance = None  # Private class variable to hold the single instance
     
    def __new__(cls) :
        if cls._instance is None :
            cls._instance = super(Logger, cls).__new__(cls)
            print("Logger created exactly once")
            return cls._instance
        else :
             print("logger already created")

    def __init__(self):
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)
        


def main():
    # Logger should only be initialized one time if it is properly
    # refactored as a singleton class
    for i in range(3):
        logger = Logger()
        


if __name__ == "__main__":
    main()
