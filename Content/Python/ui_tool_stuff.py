import unreal

def count_assets_in_folder(folder_path="/Game/"):
    assets = unreal.EditorAssetLibrary.list_assets(
        directory_path=folder_path,
        recursive=True,
        include_folder = False
    )
    count = len(assets)
    unreal.log(f"Found {count} assets in {folder_path}")
    return count

def list_asset_types(folder_path="/Game/"):
    assets = unreal.EditorAssetLibrary.list_assets(
        directory_path=folder_path,
        recursive=True,
        include_folder = False
    )

    type_counts = {}

    for asset_path in assets:
        asset_data = unreal.EditorAssetLibrary.find_asset_data(asset_path)
        class_name = str(asset_data.asset_class_path.asset_name)
        type_counts[class_name] = type_counts.get(class_name, 0) + 1
    unreal.log(f"Asset breakdown for {folder_path}")
    unreal.log("-"*50)
    for asset_type,count in sorted(type_counts.items(), key=lambda x: -x[1]):
        unreal.log(f"{asset_type}: {count}")

    return type_counts

def add_suffix_to_selected(suffix="_Spencer"):
    selected = unreal.EditorUtilityLibrary.get_selected_assets()

    if not selected:
        unreal.log_warning("No assets selected")
        return []

    renamed = []

    with unreal.ScopedEditorTransaction(f"Add suffix {suffix}") as transaction:
        for asset in selected:
            name = asset.get_name()
            path = asset.get_path_name().split(".")[0]

            if(name.endswith(suffix)):
                unreal.log(f"SKIP {name} (already has suffix)")
                continue
            new_name = name + suffix
            new_path = path.rsplit("/",1)[0] + "/" + new_name
            success = unreal.EditorAssetLibrary.rename_asset(path, new_path)

            if success:
                unreal.log(f"Renamed {name} to {new_name}")
                renamed.append(new_name)
            else: unreal.log_error(f"Can't rename; unkown error")

    unreal.log(f"Added {suffix} to {len(renamed)} assets")
    return renamed

if __name__ == "__main__":
    added = add_suffix_to_selected()
