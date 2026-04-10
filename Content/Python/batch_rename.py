import unreal




PREFIX_MAP = {
    "StaticMesh": "SM_",
    "Material": "M_",
    "Blueprint": "BP_",
    "SoundWave": "Jimmy_",
    "NiagaraSystem": "NS_"
}

def get_expected_prefix(asset):
    class_name = asset.get_class().get_name()
    return PREFIX_MAP.get(class_name, None)

def needs_rename(asset_name, prefix):
    return not asset_name.startswith(prefix)

def rename_asset(asset_path, new_name):
    new_path = asset_path.rsplit("/",1)[0] + "/" + new_name
    success = unreal.EditorAssetLibrary.rename_asset(asset_path, new_path)
    return success

selected_asset = unreal.EditorUtilityLibrary.get_selected_assets()

if len(selected_asset) == 0:
    unreal.log_warning("No asset selected :(")
else:
    renamed_count = 0
    skipped_count = 0

    for asset in selected_asset:
        asset_name = asset.get_name()
        asset_path = asset.get_path_name().split(".")[0]
        prefix = get_expected_prefix(asset)

        if prefix is None:
            unreal.log(f"Skipping {asset_name}")
            skipped_count += 1
            continue

        if not needs_rename(asset_name, prefix):
            unreal.log(f"{asset_name}already has the right prefix")
            skipped_count += 1
            continue
        new_name = prefix + asset_name
        success = rename_asset(asset_path, new_name)

        if success:
            unreal.log(f"Renamed {asset_name} to {new_name}")
            renamed_count += 1
        else:
            unreal.log(f"Failed to rename {asset_name} unknown error")

    unreal.log(f"Renamed {renamed_count} assets, skipped {skipped_count}")