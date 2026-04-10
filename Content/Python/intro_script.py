import unreal

unreal.log("Hello :)")
unreal.log("Do not eat ramen 3 days in a row :()")
unreal.log_error("There was an error")

engine_version = unreal.SystemLibrary.get_engine_version()
unreal.log(f"Running {engine_version} version")

methods = [method for method in dir(unreal.EditorAssetLibrary) if "asset" in method.lower()]
unreal.log(f"AssetMethods: {methods}")