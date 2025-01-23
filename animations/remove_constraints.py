import bpy
import os

# prepare armature - remove constraints

sceletions = bpy.context.selected_objects

for sceleton in sceletions:
    bpy.context.view_layer.objects.active = sceleton
    bpy.ops.object.posemode_toggle()
    bpy.ops.pose.select_all(action='SELECT')
    bpy.ops.nla.bake(frame_start=1, frame_end=2, visual_keying=True, clear_constraints=True, clean_curves=True, bake_types={'POSE'})
    bpy.context.view_layer.objects.active.animation_data.action = bpy.data.actions.get("anotheraction")
    bpy.ops.object.posemode_toggle()

