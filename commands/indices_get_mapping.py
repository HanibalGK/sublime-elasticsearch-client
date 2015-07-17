from .base import BaseCommand


class IndicesGetMappingCommand(BaseCommand):

    def is_enabled(self):
        return True

    def run_request(self, doc_type=None):
        if doc_type is None:
            self.show_doc_type_list_panel(self.run_request)
            return

        options = dict(
            index=self.settings.index,
            doc_type=doc_type
        )

        response = self.client.indices.get_mapping(**options)
        self.show_response(response)
