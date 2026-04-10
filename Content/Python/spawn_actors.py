import unreal

location = unreal.Vector(0.0, 0.0, 200.0)
rotation = unreal.Rotator(0.0,0.0,0.0)

light_actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
    unreal.PointLight,
    location,
    rotation
)

unreal.log(f"Spawned Light at {location}")

light_actor.set_actor_label("SuperAwesomePointLight")

mesh_location = unreal.Vector(300, 0.0, 0.0)
mesh_actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
    unreal.StaticMeshActor,
    mesh_location,
    rotation
)

mesh_actor.set_actor_label("CoolMesh")

cube_mesh = unreal.EditorAssetLibrary.load_asset(
    "/Engine/BasicShapes/Cube"
)

mesh_component = mesh_actor.get_component_by_class(unreal.StaticMeshComponent)
mesh_component.set_static_mesh(cube_mesh)

unreal.log(f"Spawned a cube at {mesh_location}")