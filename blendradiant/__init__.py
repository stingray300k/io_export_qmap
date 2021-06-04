import bpy
from .export import ExportQuakeMap, menu_func_export
from .ui import BlendRadiantObjectPropertiesPanel, \
  SearchEntityClassnamesOperator
from .mesh import MakeRoomOperator
from .props import BlendRadiantObjectProperties

bl_info = {
    "name": "BlendRadiant",
    "author": "chedap, stingray300k",
    "version": (2021, 6, 4),
    "blender": (2, 91, 0),
    "location": "File > Export",
    "description": "Export scene as (Gtk/Net)Radiant Quake map",
    "category": "Import-Export",
}

def register():
    bpy.utils.register_class(ExportQuakeMap)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)
    bpy.utils.register_class(BlendRadiantObjectProperties)
    bpy.types.Object.blendradiant = bpy.props.PointerProperty(type=BlendRadiantObjectProperties)
    bpy.utils.register_class(SearchEntityClassnamesOperator)
    bpy.utils.register_class(BlendRadiantObjectPropertiesPanel)
    bpy.utils.register_class(MakeRoomOperator)

def unregister():
    bpy.utils.unregister_class(ExportQuakeMap)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)
    bpy.utils.unregister_class(BlendRadiantObjectProperties)
    del bpy.types.Object.blendradiant
    bpy.utils.unregister_class(SearchEntityClassnamesOperator)
    bpy.utils.unregister_class(BlendRadiantObjectPropertiesPanel)
    bpy.utils.unregister_class(MakeRoomOperator)

if __name__ == "__main__":
    register()