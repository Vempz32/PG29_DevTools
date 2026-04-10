import unreal 

asset_paths = unreal.EditorAssetLibrary.list_assets(
    directory_path="/Game/",
    recursive=False,
    include_folder=False
)

unreal.log(f"Found{len(asset_paths)} in '\Game\'")
for path in asset_paths[:10]:
    unreal.log(path)
    
if len(asset_paths) > 0:
    first_asset_path = asset_paths[0]
    asset = unreal.EditorAssetLibrary.load_asset(first_asset_path)
    
    if asset:
        asset_class = asset.get_class()
        asset_name = asset.get_name()
        unreal.log(f"Loaded asset {asset_name}")
        unreal.log(f"Class {asset_class.get_name()}")
        unreal.log(f"Path{first_asset_path}")
        
        asset_data = unreal.EditorAssetLibrary.find_asset_data(first_asset_path)
        unreal.log("Via findAssetData")
        unreal.log(asset_data.package_name)

    test_asset = "/Game/sponder.sponder"
    exists = unreal.EditorAssetLibrary.does_asset_exist(test_asset)
    unreal.log(f"{test_asset} exists? {exists}")

    #EditorAssetLibrary
    #EditorLevelLibrary
    #EditorUtilityLibrary
    #SystemLibrary

    selected_asset = unreal.EditorUtilityLibrary.get_selected_assets()
    for asset in selected_asset:
        unreal.log(f"{asset.get_name()} ({asset.get_class().get_name()})")