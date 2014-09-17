from ansible.runner.return_data import ReturnData


class ActionModule(object):
    def __init__(self, runner):
        self.runner = runner
        self.runner.run_once = True

    def run(self, conn, tmp, module_name, module_args, inject, complex_args=None, **kwargs):
        return ReturnData(conn=conn,
                          comm_ok=True,
                          result=dict(failed=False, changed=False, msg="YOLO"))
