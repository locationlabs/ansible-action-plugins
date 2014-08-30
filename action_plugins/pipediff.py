from ansible.runner.return_data import ReturnData


class ActionModule(object):
    def __init__(self, runner):
        self.runner = runner

    def run(self, conn, tmp, module_name, module_args, inject, complex_args=None, **kwargs):
        response = self.runner._execute_module(conn,
                                               tmp,
                                               "pipediff",
                                               module_args,
                                               inject=inject)
        before = response.result.pop('before', '')
        after = response.result.pop('after', '')
        return ReturnData(conn=conn,
                          comm_ok=response.comm_ok,
                          result=response.result,
                          diff=dict(before=before,
                                    after=after))
