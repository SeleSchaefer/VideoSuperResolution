#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Simon Schaefer
# Description : DIV2K validation dataset extension.
# =============================================================================
import os

from tar.dataloader import _Dataset_

class VDIV2K(_Dataset_):
    def __init__(self, args, train, scale, name="VDIV2K"):
        super(VDIV2K, self).__init__(args, name=name, train=train, scale=scale)

    def _scan(self):
        names_hr, names_lr = super(VDIV2K, self)._scan()
        return names_hr, names_lr

    def _set_filesystem(self, dir_data):
        super(VDIV2K, self)._set_filesystem(dir_data)
        self.directory = os.path.join(self.args.dir_data, "DIV2K")
        self.dir_hr = os.path.join(self.directory, 'DIV2K_valid_HR')
        self.dir_lr = os.path.join(self.directory, 'DIV2K_valid_LR_bicubic')
        self.dir_lr = os.path.join(self.dir_lr, "X{}".format(self.scale))
