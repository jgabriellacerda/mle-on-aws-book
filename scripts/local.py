import argparse
from pathlib import Path
import subprocess
import sys
from sagify.config.config import ConfigManager  # type: ignore


def local_deploy(args: argparse.Namespace):
    """Deploys using a subprocess and reads logs concurrently."""
    deploy_script = Path.cwd() / "local_test" / "deploy_local.sh"

    command = [
        str(deploy_script),
        args.test_path,
        args.tag,
        args.image,
    ]
    process = subprocess.Popen(command, stdout=sys.stdout, stderr=sys.stderr, text=True)
    process.wait()
    print("Process completed.")


def local():
    config = ConfigManager(".sagify.json").get_config()

    argparser = argparse.ArgumentParser(description="Run the image locally.")
    subparsers = argparser.add_subparsers(dest="subcommand")

    test_path = Path.cwd() / "local_test" / "test_dir"

    deploy_parser = subparsers.add_parser("deploy")
    deploy_parser.add_argument(
        "--test_path",
        type=str,
        help="The path to the local test folder.",
        default=str(test_path),
    )
    deploy_parser.add_argument(
        "--tag",
        type=str,
        default="latest",
        help="The tag of the image to deploy.",
    )
    deploy_parser.add_argument(
        "--image",
        type=str,
        default=config.image_name,
        help="The name of the image to deploy.",
    )

    deploy_parser.set_defaults(func=local_deploy)

    args = argparser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        argparser.print_help()
