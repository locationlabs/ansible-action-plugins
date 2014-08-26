from ansible.runner.return_data import ReturnData


class ActionModule(object):
    def __init__(self, runner):
        self.runner = runner

    def run(self, conn, tmp, module_name, module_args, inject, complex_args=None, **kwargs):
        result = {"failed": False, "changed": False}
        result.update(inject)
        return ReturnData(conn=conn,
                          comm_ok=True,
                          result=result)
