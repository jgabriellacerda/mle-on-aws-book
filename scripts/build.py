import argparse
from pathlib import Path
import subprocess
from sagify.config.config import ConfigManager  # type: ignore


def build():
    config = ConfigManager(".sagify.json").get_config()

    argparser = argparse.ArgumentParser(description="Build the image.")
    argparser.add_argument(
        "--dockerfile-path",
        type=str,
        default="Dockerfile",
        help="The path to the Dockerfile.",
    )
    argparser.add_argument(
        "--tag", type=str, default="latest", help="The tag of the image to build."
    )
    argparser.add_argument(
        "--image",
        type=str,
        default=config.image_name,
        help="The name of the image to build.",
    )

    args = argparser.parse_args()

    build_script = Path.cwd() / "build.sh"

    output = subprocess.check_output(
        [
            str(build_script),
            args.dockerfile_path,
            args.tag,
            args.image,
        ]
    )
    print(output.decode("utf-8"))
