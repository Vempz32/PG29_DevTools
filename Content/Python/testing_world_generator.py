import unreal
import sys
location = unreal.Vector(0.0, 0.0, 0.0)
rotation = unreal.Rotator(0.0, 0.0, 0.0)

LevelTitle = sys.argv[1] if len(sys.argv) > 1 else ""

if LevelTitle != "" :
    map_path = f"/Game/Maps/{LevelTitle}"
    testing_level = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
    success = testing_level.new_level(map_path)

    sun_actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
    unreal.DirectionalLight,
    location,
    rotation,
    )

    sun_actor.set_actor_label("Sun")

    sky_light_actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
    unreal.SkyLight,
    location,
    rotation,
    )
    sky_light_actor.set_actor_label("Sky Light")

    sky_atomsphere_actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
    unreal.SkyAtmosphere,
    location,
    rotation,
    )
    sky_atomsphere_actor.set_actor_label("Sky Atomsphere")

    height_fog_actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
    unreal.ExponentialHeightFog,
    location,
    rotation,
    )
    height_fog_actor.set_actor_label("Height Fog")

    volumetric_cloud_actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
    unreal.VolumetricCloud,
    location,
    rotation,
    )
    volumetric_cloud_actor.set_actor_label("Volumetric Clouds")

    ground_actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
    unreal.StaticMeshActor,
    location,
    rotation,
    )

    ground_actor.set_actor_label("Ground")

    cube_mesh = unreal.EditorAssetLibrary.load_asset(
    "/Engine/BasicShapes/Cube"
    )

    mesh_component = ground_actor.get_component_by_class(unreal.StaticMeshComponent)
    mesh_component.set_static_mesh(cube_mesh)
    mesh_component.set_relative_scale3d(unreal.Vector(200.0,200.0,1.0))



    sun_actor.set_folder_path("/Lighting")
    sky_light_actor.set_folder_path("/Lighting")
    sky_atomsphere_actor.set_folder_path("/Lighting")
    height_fog_actor.set_folder_path("/Lighting")
    volumetric_cloud_actor.set_folder_path("/Lighting")
    ground_actor.set_folder_path("/WorldMeshs")