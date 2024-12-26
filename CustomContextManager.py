class ContextManager:
    def __init__(self, filename: str):
        pass

    def __enter__(self):
        print('Entered to context manager, initiating the resources')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exiting from context manager, releasing the resources')

def main() -> None:
    with ContextManager('sample.txt') as context:
        print('Inside the context, processing')

if __name__ == '__main__':
    main()
