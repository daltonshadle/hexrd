import os

try:
    import dill as cpl
except(ImportError):
    import cPickle as cpl

from .config import Config


class MaterialConfig(Config):

    @property
    def definitions(self):
        temp = self._cfg.get('material:definitions')
        if not os.path.isabs(temp):
            temp = os.path.join(self._cfg.working_dir, temp)
        if os.path.exists(temp):
            return temp
        raise IOError(
            '"material:definitions": "%s" does not exist'
            )

    @property
    def active(self):
        return self._cfg.get('material:active')

    @property
    def plane_data(self):
        with file(self.definitions, "r") as matf:
            mat_list = cpl.load(matf)
        return dict(zip([i.name for i in mat_list], mat_list))[self.active].planeData
