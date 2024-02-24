import syft as sy
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()
    environment = os.environ["ENV"]
    server_name = os.environ["SERVER_NAME"]
    port = int(os.environ["PORT"])
    sy.requires(os.environ["VERSION"])
    if environment == "PROD":
        node = sy.orchestra.launch(name=server_name, port=port, reset=True)
    else:
        node = sy.orchestra.launch(
            name=server_name, port=port, dev_mode=True, reset=True
        )
