class DashHandler:

    def __init__(self):
        self.show_modal = False
        self.title_modal = ''
        self.descr_modal = ''

    def callback(self, trigger, *args):
        if "close-modal" in trigger["prop_id"]:
            self.show_modal = False
        else:
            try:
                self._execute_callback(trigger, *args)
            except Exception as e:
                self.show_modal = True
                self.title_modal = 'Error inesperadisimo rey'
                self.descr_modal = str(type(e)) + str(e)

        return self._get_response()

    def _execute_callback(self, *args):
        raise Exception("subclass responsiblity")

    def _get_response(self):
        raise Exception("subclass responsiblity")
