import bpy
import os

# prepare armature - remove constraints

bpy.ops.object.select_pattern(pattern="Skeleton.*", extend=False)
sceletons = bpy.context.selected_objects

for sceleton in sceletons:
    bpy.context.view_layer.objects.active = sceleton
    bpy.ops.object.posemode_toggle()
    bpy.ops.pose.select_all(action='SELECT')
    bpy.ops.nla.bake(frame_start=1, frame_end=2, only_selected=True, visual_keying=True, clear_constraints=True, clean_curves=True, bake_types={'POSE'})
    bpy.context.view_layer.objects.active.animation_data.action = bpy.data.actions.get("anotheraction")
    bpy.ops.object.posemode_toggle()
    
bpy.ops.object.select_all(action='DESELECT')

# export

basedir = os.path.dirname(bpy.data.filepath)

if not basedir:
    raise Exception("Blend file is not saved")

# make export dir
exp_dir_name = "export_hair_girl"

exp_dir = os.path.join(basedir, exp_dir_name)
if not os.path.isdir(str(exp_dir)):
    os.mkdir(str(exp_dir))

# select all for export
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_pattern(pattern="Skeleton.Hair.*", extend=True)
bpy.ops.object.select_pattern(pattern="hair.*", extend=True)

file_name = "hair_common"
out_file = os.path.join(exp_dir, file_name)

bpy.ops.export_scene.gltf(filepath=out_file + ".gltf", check_existing=False, export_import_convert_lighting_mode='SPEC', gltf_export_id="", export_format='GLTF_SEPARATE', ui_tab='GENERAL', export_copyright="@serufu_yua", export_image_format='AUTO', export_texture_dir="", export_jpeg_quality=75, export_keep_originals=False, export_texcoords=True, export_normals=True, export_draco_mesh_compression_enable=False, export_draco_mesh_compression_level=6, export_draco_position_quantization=14, export_draco_normal_quantization=10, export_draco_texcoord_quantization=12, export_draco_color_quantization=10, export_draco_generic_quantization=12, export_tangents=True, export_materials='EXPORT', export_original_specular=False, export_colors=False, export_attributes=False, use_mesh_edges=False, use_mesh_vertices=False, export_cameras=False, use_selection=True, use_visible=False, use_renderable=False, use_active_collection_with_nested=False, use_active_collection=False, use_active_scene=False, export_extras=False, export_yup=True, export_apply=True, export_animations=True, export_frame_range=False, export_frame_step=1, export_force_sampling=True, export_animation_mode='NLA_TRACKS', export_nla_strips_merged_animation_name="Animation", export_def_bones=True, export_hierarchy_flatten_bones=False, export_optimize_animation_size=True, export_optimize_animation_keep_anim_armature=True, export_optimize_animation_keep_anim_object=True, export_negative_frame='SLIDE', export_anim_slide_to_zero=False, export_bake_animation=False, export_anim_single_armature=True, export_reset_pose_bones=True, export_current_frame=False, export_rest_position_armature=True, export_anim_scene_split_object=True, export_skins=True, export_all_influences=False, export_morph=False, export_morph_normal=True, export_morph_tangent=False, export_morph_animation=True, export_morph_reset_sk_data=True, export_lights=False, export_nla_strips=True, will_save_settings=False, filter_glob="*.gltf")
