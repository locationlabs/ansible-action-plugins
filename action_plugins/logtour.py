from ansible.runner.return_data import ReturnData
from ansible.callbacks import vv, vvv, vvvv
from ansible.callbacks import verbose


def vvvvv(msg, host=None):
    return verbose(msg, host=host, caplevel=4)


class ActionModule(object):
    def __init__(self, runner):
        self.runner = runner

    def run(self, conn, tmp, module_name, module_args, inject, complex_args=None, **kwargs):
        vv("Kind of verbose")
        vvv("Verbose")
        vvvv("Lookout!")
        vvvvv("Super custom verbosity")
        return ReturnData(conn=conn,
                          comm_ok=True,
                          result={"failed": False, "changed": False})
