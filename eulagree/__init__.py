import os

from mcdreforged.api.types import PluginServerInterface
from ruamel import yaml


def on_load(server: PluginServerInterface, _):
    with open("config.yml") as f:
        mcdr_config = yaml.safe_load(f)
    working_directory = mcdr_config["working_directory"]
    with open(os.path.join(working_directory, "eula.txt"), "w", encoding="utf8") as f:
        f.write("eula=true")
    server.unload_plugin("eulagree")
