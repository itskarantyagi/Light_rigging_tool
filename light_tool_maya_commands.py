import maya.cmds as cmds
import sys
import final_light_setup

reload(final_light_setup)
from final_light_setup import Final_tool

from PySide2.QtWidgets import (QApplication, QComboBox, QDialog,
QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
QVBoxLayout, QRadioButton)


class Light_tool_maya_commands(Final_tool):

    def __init__(self, *args):
        Final_tool.__init__(self, *args)
        # print self.create_btn, "the inherited button"
        self.get_data = self.fetch
        # self.show()
        self.get_characters = self.update_characters
        # self.shadow_action = self.user_shadow

    # def user_shadow(self):

    def update_characters(self):

        if (self.choice1 == 'Character'):
            
            self.optional_widget_combo.addItems(cmds.ls("*global_ctrl"))

    def fetch(self):
        print("entering fetch")
        rig_choice = self.top2.currentText()
        

        if rig_choice == "3 Point":
            print("Entering 3 Point")
            self.user_dict = {rig_choice: {
                self.f_label.text(): self.f_field.text(),
                self.s_label.text(): self.s_field.text(),
                self.t_label.text(): self.t_field.text(),
                "Fixed/Character": self.choice1
            }}

            if (self.choice1 == 'Character'):
                self.light_values = self.Combo.currentIndexChanged.connect(self.character_light_setup)

            key = cmds.spotLight(i=float(self.f_field.text()), name='key_light')
            fill = cmds.spotLight(i=float(self.s_field.text()), name='fill_light')
            rim = cmds.spotLight(i=float(self.t_field.text()), name='rim_light')
            cmds.setAttr("{0}.useRayTraceShadows".format(fill), 0)
            cmds.setAttr("{0}.useRayTraceShadows".format(rim), 0)
            key_tr = cmds.listRelatives(key, p=True)[0]
            fill_tr = cmds.listRelatives(fill, p=True)[0]
            rim_tr = cmds.listRelatives(rim, p=True)[0]

            key_loc = cmds.spaceLocator(n="{0}_aim".format(key_tr))[0]
            fill_loc = cmds.spaceLocator(n="{0}_aim".format(fill_tr))[0]
            rim_loc = cmds.spaceLocator(n="{0}_aim".format(rim_tr))[0]

            key_grp = cmds.group(key_tr, name="key_lit_grp")
            fill_grp = cmds.group(fill_tr, name="fill_lit_grp")
            rim_grp = cmds.group(rim_tr, name="rim_lit_grp")

            cmds.xform(key_tr, ws=True, t=(10, 10, 7))
            cmds.xform(fill_tr, ws=True, t=(-10, -6, 5))
            cmds.xform(rim_tr, ws=True, t=(10, 10, -7))

            cmds.aimConstraint(key_loc, key_tr, mo=False,
                               aim=(0, 0, -1))
            cmds.aimConstraint(fill_loc, fill_tr, mo=False,
                               aim=(0, 0, -1))
            cmds.aimConstraint(rim_loc, rim_tr, mo=False,
                               aim=(0, 0, -1))

            cmds.group([key_loc, fill_loc, rim_loc, key_grp, fill_grp, rim_grp], name='three_point_light_rig')

        elif rig_choice == "Fake GI":
            print("Entering Fake GI")
            self.user_dict = {rig_choice: {
                self.f_label.text(): self.f_field.currentText(),
                self.s_label.text(): self.s_field.text(),
                self.t_label.text(): self.t_field.text(),
                "Light Type": self.light_type_combo.currentText(),
                "Shadow type": self.options_for_shadowtype.currentText()
            }}


            radius = float(self.s_field.text())
            intensity = float(self.t_field.text())
            count_data = {}

            for c, i in enumerate(range(3, 21)):
                print(i * (i - 1) + 2)
                count_data[i * (i - 1) + 2] = i

            try:
                light_count = int(self.f_field.currentText())
            except:
                msg = QDialog()
                msg.setFixedSize(300, 100)
                vl = QVBoxLayout()
                msg_txt = QLabel("Please Select Number of Lights.")
                vl.addWidget(msg_txt)
                ok_btn = QPushButton("Ok")
                ok_btn.clicked.connect(msg.close)
                vl.addWidget(ok_btn)
                msg.setLayout(vl)
                msg.setModal(True)
                msg.show()

            cmds.polySphere(r=radius, sx=count_data[light_count], sy=count_data[light_count])

            obj = cmds.ls(sl=True)
            vtxes = cmds.ls("{0}.vtx[*]".format(obj[0]), fl=True)
            lights = []
            for vtx in vtxes:
                pos = cmds.xform(vtx, ws=True, q=True, t=True)

                choice = self.light_type_combo.currentText()

                if choice == 'Directional':
                    sl = cmds.directionalLight(i=intensity)
                elif choice == 'Spot':
                    sl = cmds.spotLight(i=intensity)
                    # resolution = int(self.shadow_type_resolution_field.text())

                    # filter_size = float(self.shadow_type_filtersize_field.text())

                    if self.shadowtype_choice == "Depth Map":
                        cmds.setAttr("{0}.useDepthMapShadows".format(sl), 1)

                        try:
                            resolution = int(self.shadow_type_resolution_field.text())
                        except:
                            msg = QDialog()
                            msg.setFixedSize(350, 100)
                            vl = QVBoxLayout()
                            msg_txt = QLabel("Please enter Resolution/ Datatype entered is not supported")
                            vl.addWidget(msg_txt)
                            ok_btn = QPushButton("Ok")
                            ok_btn.clicked.connect(msg.close)
                            vl.addWidget(ok_btn)
                            msg.setLayout(vl)
                            msg.setModal(True)
                            msg.show()

                        cmds.setAttr("{0}.dmapResolution".format(sl), resolution)

                        try:
                            filter_size = float(self.shadow_type_filtersize_field.text())
                        except:
                            msg = QDialog()
                            msg.setFixedSize(350, 100)
                            vl = QVBoxLayout()
                            msg_txt = QLabel("Please enter Filter size/ Datatype entered is not supported")
                            vl.addWidget(msg_txt)
                            ok_btn = QPushButton("Ok")
                            ok_btn.clicked.connect(msg.close)
                            vl.addWidget(ok_btn)
                            msg.setLayout(vl)
                            msg.setModal(True)
                            msg.show()

                        cmds.setAttr("{0}.dmapFilterSize".format(sl), filter_size)

                elif choice == 'Area':
                    sl = cmds.shadingNode('areaLight', asLight=True)
                else:
                    sl = cmds.directionalLight(i=intensity)
                if choice == 'Area':
                    sl_tr = sl
                else:
                    sl_tr = cmds.listRelatives(sl, p=True)[0]
                cmds.xform(sl_tr, ws=True, t=pos)
                loc = cmds.spaceLocator()
                con = cmds.aimConstraint(loc[0], sl_tr, aim=(0, 0, -1))
                cmds.delete(con, loc)
                lights.append(sl_tr)
            cmds.delete(obj)
            cmds.group(lights, name="GeoJo")

        elif rig_choice == "IBL":

            self.user_dict = {rig_choice: {
                self.radius_label.text(): self.radius_field.text(),
                self.hdr_image_label.text(): self.hdr_image_field.text()
            }}

            radius = float(self.radius_field.text())

            path = str(self.hdr_image_field.text())
            res = cmds.polySphere(r=radius)
            lam = cmds.shadingNode('lambert', asShader=True)
            cmds.select(res[0])
            cmds.hyperShade(assign=lam)
            cmds.setAttr("{0}.diffuse".format(lam), 0)
            fl = cmds.shadingNode('file', asTexture=True)
            cmds.connectAttr("{0}.outColor".format(fl), "{0}.incandescence".format(lam))
            cmds.setAttr("{0}.ftn".format(fl), path, type='string')

        else:
            pass
        self.create_point_lights()
        return self.user_dict

    def create_point_lights(self):
        for k, v in self.user_dict.items():
            print(k, v)
            for ik, iv in v.items():
                print(ik, iv)

    def character_light_setup(self):
        choice = self.Combo.currentText()
        cmds.select(choice)
        translation = cmds.getAttr({0}.format(choice))
        return translation

    def error_correction(self, type="", text_field_name="", message=""):

        if type == "int":

            try:
                variable = float("{0}.currentText()".format(text_field_name))
            except:
                msg = QDialog(self)
                msg.setFixedSize(300, 100)
                vl = QVBoxLayout()
                msg_txt = QLabel(message)
                vl.addWidget(msg_txt)
                ok_btn = QPushButton("Ok")
                ok_btn.clicked.connect(msg.close)
                vl.addWidget(ok_btn)
                msg.setLayout(vl)
                msg.setModal(True)
                msg.show()

        if type == "float":
            try:
                variable = float("{0}.currentText()".format(text_field_name))
            except:
                msg = QDialog(self)
                msg.setFixedSize(300, 100)
                vl = QVBoxLayout()
                msg_txt = QLabel(message)
                vl.addWidget(msg_txt)
                ok_btn = QPushButton("Ok")
                ok_btn.clicked.connect(msg.close)
                vl.addWidget(ok_btn)
                msg.setLayout(vl)
                msg.setModal(True)
                msg.show()
            return variable


if __name__ == "__main__":
    app = QApplication([])
    # mw = QMainWindow()
    wdg = Light_tool_maya_commands()
    wdg.show()
    sys.exit(app.exec_())


