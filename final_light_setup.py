import sys

from PySide2.QtWidgets import (QApplication,QWidget, QComboBox, QDialog, QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                   QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit, QVBoxLayout, QRadioButton)


from PySide2.QtGui import *
from PySide2.QtCore import *



class Final_tool(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setup_ui()
        self.field = None
        self.i = None
        self.f_label = None
        self.f_field = None
        self.f_layout = None
        self.s_label = None
        self.s_field = None
        self.s_layout = None
        self.t_label = None
        self.t_field = None
        self.t_layout = None
        self.radio = None
        self.light_type = None
        self.radiobtn = None
        self.radio = None
        self.radio_list = []
        self.btn1 = None
        self.btn2 = None
        self.light_type_label = None
        self.light_type_combo = None
        self.light_type_hl = None
        self.radius_field = None
        self.radius_label = None
        self.radius_layout = None
        self.hdr_image_field = None
        self.hdr_image_label = None
        self.hdr_layout = None
        self.push_ibl = None
        self.selected_btn = None
        self.optional_widget_label = None
        self.optional_widget_combo = None
        self.optional_widget_layout = None
        self.shadowtype = None
        self.create_btn = None
        self.create_btn_hl = None
        self.hl = None
        self.shadow_hl1 = None
        self.shadow_hl = None
        self.hl1 = None
        self.shadow_type_filtersize = None
        self.shadow_type_resolution_field = None
        self.shadow_type_resolution = None
        self.shadow_type_filtersize_field = None
        self.options_for_shadowtype = None
        self.option_shadowtype_layout = None
        self.label_shadow_option = None

    def get_characters(self):
        print('getting characters in UI')
        pass

    def get_data(self):
        pass

    def setup_ui(self):
        self.main_vl = QVBoxLayout()
        self.top_hl = QHBoxLayout()
        self.top1 = QLabel()
        self.top1.setText("Rigtype")
        self.top2 = QComboBox()
        self.top2.addItem("Select")
        self.top2.addItem("3 Point")
        self.top2.addItem("Fake GI")
        self.top2.addItem("IBL")
        self.top2.currentIndexChanged.connect(self.rigs)
        self.top_hl.addWidget(self.top1)
        self.top_hl.addWidget(self.top2)
        self.main_vl.addLayout(self.top_hl)
        self.setLayout(self.main_vl)

    def push_btn(self, name):
        print('push button creation')
        hl = QHBoxLayout()
        name_of_btn = QPushButton(name)
        print(name_of_btn, "HI")
        hl.addWidget(name_of_btn)
        self.main_vl.addLayout(hl)
        name_of_btn.clicked.connect(self.get_data)
        # print name_of_btn, "within push button method"
        return name_of_btn, hl

    def Radiobtn(self, radio=[]):

        radio_list = []
        hl = QHBoxLayout()

        for i in radio:
            radiobtn = QRadioButton(i)
            radiobtn.clicked.connect(self.action)
            radio_list.append(radiobtn)
            hl.addWidget(radiobtn)
        self.main_vl.addLayout(hl)
        radio_list.append(hl)
        return radio_list

    def action(self):
        self.choice1 = self.sender().text()

        if self.choice1 == "Character":
            self.delete_lab_text(
                objects=[[self.optional_widget_label, self.optional_widget_combo, self.optional_widget_layout]])
            self.delete_lab_text(objects=[[self.create_btn_hl, self.create_btn]])
            self.optional_widget_label, self.optional_widget_combo, self.optional_widget_layout = self.lab_combo(
                lab="List of characters", option=[])

        elif self.choice1 == 'Fixed':
            self.delete_lab_text(objects=[[self.create_btn_hl, self.create_btn]])
            self.delete_lab_text(
                objects=[[self.optional_widget_layout, self.optional_widget_combo, self.optional_widget_label]])

            print("doing for area light")
        else:
            pass
        self.create_btn, self.create_btn_hl = self.push_btn(name="Create")
        print(self.create_btn, "not inherited_1")

    def lab_combo(self, lab="", option=[]):

        self.hl = QHBoxLayout()
        self.label = QLabel()
        self.label.setText(lab)

        self.Combo = QComboBox()
        for i in option:
            self.Combo.addItem(i)
        self.hl.addWidget(self.label)
        self.hl.addWidget(self.Combo)
        self.main_vl.addLayout(self.hl)
        return self.label, self.Combo, self.hl

    def lab_text(self, label="", text=""):

        self.hl = QHBoxLayout()
        self.label = QLabel()
        self.label.setText(label)
        self.field = QLineEdit(text)
        self.hl.addWidget(self.label)
        self.hl.addWidget(self.field)
        self.main_vl.addLayout(self.hl)
        return self.label, self.field, self.hl

    def shadow_action(self):
        self.delete_lab_text(
            objects=[[self.shadow_type_filtersize, self.shadow_type_resolution_field,
                      self.shadow_type_resolution, self.shadow_type_filtersize_field]])
        self.delete_lab_text(objects=[[self.create_btn_hl, self.create_btn], [self.shadow_hl, self.shadow_hl1]])
        self.shadowtype_choice = self.sender().currentText()
        if self.shadowtype_choice == 'Depth Map':
            self.shadow_hl = QHBoxLayout()
            self.shadow_hl1 = QHBoxLayout()
            self.shadow_type_resolution = QLabel()
            self.shadow_type_resolution.setText("Resolution")
            self.shadow_type_resolution_field = QLineEdit("512")
            self.shadow_hl.addWidget(self.shadow_type_resolution)
            self.shadow_hl.addWidget(self.shadow_type_resolution_field)
            self.main_vl.addLayout(self.shadow_hl)
            self.shadow_type_filtersize = QLabel()
            self.shadow_type_filtersize.setText("Filter Size")
            self.shadow_type_filtersize_field = QLineEdit("1")
            self.shadow_hl1.addWidget(self.shadow_type_filtersize)
            self.shadow_hl1.addWidget(self.shadow_type_filtersize_field)
            self.main_vl.addLayout(self.shadow_hl1)
            self.create_btn, self.create_btn_hl = self.push_btn(name="Create")
        else:
            self.create_btn, self.create_btn_hl = self.push_btn(name="Create")

    def fakegi_widget(self):
        print("Entering fake gi widget")
        choice = self.light_type_combo.currentText()

        if choice == 'Directional' or choice == 'Area':
            self.delete_lab_text(objects=[[self.create_btn_hl, self.create_btn]])
            self.delete_lab_text(
                objects=[
                    [self.shadow_type_filtersize, self.shadow_type_resolution_field, self.shadow_hl, self.shadow_hl1,
                     self.shadow_type_resolution, self.shadow_type_filtersize_field],
                    [self.create_btn_hl, self.create_btn],
                    [self.options_for_shadowtype, self.option_shadowtype_layout, self.label_shadow_option]])
            self.option_shadowtype_layout = QHBoxLayout()
            self.label_shadow_option = QLabel()
            self.label_shadow_option.setText("Shadow Type")
            self.options_for_shadowtype = QComboBox()

            self.options_for_shadowtype.addItem("Ray Trace")
            self.option_shadowtype_layout.addWidget(self.label_shadow_option)

            self.option_shadowtype_layout.addWidget(self.options_for_shadowtype)
            self.main_vl.addLayout(self.option_shadowtype_layout)
            self.create_btn, self.create_btn_hl = self.push_btn(name="Create")

        elif choice == 'Spot':
            self.delete_lab_text(objects=[[self.create_btn_hl, self.create_btn]])
            self.delete_lab_text(
                objects=[
                    [self.shadow_type_filtersize, self.shadow_type_resolution_field, self.shadow_hl, self.shadow_hl1,
                     self.shadow_type_resolution, self.shadow_type_filtersize_field],
                    [self.create_btn_hl, self.create_btn],
                    [self.options_for_shadowtype, self.option_shadowtype_layout, self.label_shadow_option]])
            self.option_shadowtype_layout = QHBoxLayout()
            self.label_shadow_option = QLabel()
            self.label_shadow_option.setText("Shadow Type")
            self.options_for_shadowtype = QComboBox()
            self.options_for_shadowtype.addItem("Select")
            self.options_for_shadowtype.addItem("Depth Map")
            self.options_for_shadowtype.addItem("Ray Trace")
            self.option_shadowtype_layout.addWidget(self.label_shadow_option)
            self.option_shadowtype_layout.addWidget(self.options_for_shadowtype)
            self.main_vl.addLayout(self.option_shadowtype_layout)
            self.options_for_shadowtype.currentIndexChanged.connect(self.shadow_action)



        else:
            self.delete_lab_text(objects=[[self.create_btn_hl, self.create_btn]])
            # self.delete_lab_text(objects=[[self.shadowtype]])
            pass

        # print(self.create_btn, "not inherited_2")

    def rigs(self):
        # print "its working fine right now"
        choice = self.top2.currentText()
        if choice == '3 Point':
            # self.delete_lab_text(objects=[[self.light_type_label, self.light_type_combo, self.light_type_hl]])
            self.delete_lab_text(
                objects=[[self.f_label, self.f_field, self.f_layout], [self.s_label, self.s_field, self.s_layout],
                         [self.t_label, self.t_field, self.t_layout], [self.btn1],
                         [self.light_type_label, self.light_type_combo, self.light_type_hl],
                         [self.radius_label, self.radius_field, self.radius_layout],
                         [self.hdr_image_label, self.hdr_image_field, self.hdr_layout], [self.selected_btn],
                         [self.push_ibl],
                         [self.optional_widget_label, self.optional_widget_layout, self.optional_widget_combo],
                         [self.create_btn, self.create_btn_hl], [self.shadowtype],
                         [self.hl1, self.shadow_type_filtersize, self.shadow_type_resolution_field, self.hl,
                          self.shadow_type_resolution, self.shadow_type_filtersize_field],
                         [self.option_shadowtype_layout, self.options_for_shadowtype, self.label_shadow_option]])
            self.f_label, self.f_field, self.f_layout = self.lab_text('Key', '1.0')
            self.s_label, self.s_field, self.s_layout = self.lab_text('Rim', '1.0')
            self.t_label, self.t_field, self.t_layout = self.lab_text('Fill', '1.0')
            self.btn1 = self.Radiobtn(radio=["Fixed", "Character"])
            self.btn1[1].clicked.connect(self.get_characters)

            print(self.btn1)

            print("Getting out of 3 Point")

        if choice == 'Fake GI':
            self.delete_lab_text(objects=[self.btn1])
            # self.delete_lab_text([[self.radius_label, self.radius_field, self.radius_layout],
            #                       [self.hdr_image_label, self.hdr_image_field, self.hdr_layout],
            #                       [self.create_btn, self.create_btn_hl]])
            self.delete_lab_text(
                objects=[[self.f_label, self.f_field, self.f_layout], [self.s_label, self.s_field, self.s_layout],
                         [self.t_label, self.t_field, self.t_layout], [self.btn1],
                         [self.light_type_label, self.light_type_combo, self.light_type_hl],
                         [self.radius_label, self.radius_field, self.radius_layout],
                         [self.hdr_image_label, self.hdr_image_field, self.hdr_layout], [self.selected_btn],
                         [self.push_ibl],
                         [self.optional_widget_label, self.optional_widget_layout, self.optional_widget_combo],
                         [self.create_btn, self.create_btn_hl], [self.shadowtype],
                         [self.hl1, self.shadow_type_filtersize, self.shadow_type_resolution_field, self.hl,
                          self.shadow_type_resolution, self.shadow_type_filtersize_field],
                         [self.option_shadowtype_layout, self.options_for_shadowtype, self.label_shadow_option]])
            self.f_label, self.f_field, self.f_layout = self.lab_combo(lab="Number of Lights",
                                                                       option=['Select', '14', '22', '32', '44', '58',
                                                                               '74', '92', '112', '134', '158', '184',
                                                                               '212', '242', '274', '308', '344',
                                                                               '382'])
            self.s_label, self.s_field, self.s_layout = self.lab_text('Radius', '10.0')
            self.t_label, self.t_field, self.t_layout = self.lab_text('Intensity', '1.0')
            self.light_type_label, self.light_type_combo, self.light_type_hl = self.lab_combo(
                lab='Light Type (Default : Directional)',
                option=['Select',
                        'Directional',
                        'Spot', 'Area'])
            self.light_type_combo.currentIndexChanged.connect(self.fakegi_widget)
            print("Getting out of fake Gi")

        if choice == 'IBL':
            self.delete_lab_text(objects=[self.btn1])
            # self.delete_lab_text(objects=[[self.light_type_label, self.light_type_combo, self.light_type_hl]])
            self.delete_lab_text(
                objects=[[self.f_label, self.f_field, self.f_layout], [self.s_label, self.s_field, self.s_layout],
                         [self.t_label, self.t_field, self.t_layout], [self.btn1],
                         [self.light_type_label, self.light_type_combo, self.light_type_hl],
                         [self.radius_label, self.radius_field, self.radius_layout],
                         [self.hdr_image_label, self.hdr_image_field, self.hdr_layout], [self.selected_btn],
                         [self.push_ibl],
                         [self.optional_widget_label, self.optional_widget_layout, self.optional_widget_combo],
                         [self.create_btn, self.create_btn_hl], [self.shadowtype],
                         [self.hl1, self.shadow_type_filtersize, self.shadow_type_resolution_field, self.hl,
                          self.shadow_type_resolution, self.shadow_type_filtersize_field],
                         [self.option_shadowtype_layout, self.options_for_shadowtype, self.label_shadow_option]])

            self.radius_label, self.radius_field, self.radius_layout = self.lab_text('Radius', '1.0')
            self.hdr_image_label, self.hdr_image_field, self.hdr_layout = self.lab_text('HDR Image', '/u/ktya/path')
            # print("Create btn not getting created")
            self.create_btn, self.create_btn_hl = self.push_btn(name="Create")
            # print("Create btn created")
            print("Getting out of IBL")

        if choice == 'Select':
            self.delete_lab_text(
                objects=[[self.f_label, self.f_field, self.f_layout], [self.s_label, self.s_field, self.s_layout],
                         [self.t_label, self.t_field, self.t_layout], self.btn1,
                         [self.light_type_label, self.light_type_combo, self.light_type_hl],
                         [self.radius_label, self.radius_field, self.radius_layout],
                         [self.hdr_image_label, self.hdr_image_field, self.hdr_layout], [self.selected_btn],
                         [self.push_ibl],
                         [self.optional_widget_label, self.optional_widget_layout, self.optional_widget_combo],
                         [self.create_btn, self.create_btn_hl], [self.shadowtype],
                         [self.hl1, self.shadow_type_filtersize, self.shadow_type_resolution_field, self.hl,
                          self.shadow_type_resolution, self.shadow_type_filtersize_field],
                         [self.option_shadowtype_layout, self.options_for_shadowtype, self.label_shadow_option]])

    def delete_lab_text(self, objects=[]):
        for obj in objects:
            if not obj:
                return
            for ob in obj:
                try:
                    ob.setParent(None)
                    ob.deleteLater()
                except:
                    pass


if __name__ == "__main__":
    # print "this i s final_light_setup main file"
    app = QApplication([])
    # mw = QMainWindow()
    wdg = Final_tool()
    wdg.show()
    sys.exit(app.exec_())
else:
    print("its inherited in light_tool_maya_command")
