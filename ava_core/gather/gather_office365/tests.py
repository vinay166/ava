# Rest Imports
# Local Imports
from rest_framework.reverse import reverse

from ava_core.abstract.test import AvaCoreTest
from ava_core.gather.gather_office365.test_data import Office365GatherHistoryTestData
# Implementation
from ava_core.integration.integration_office365.test_data import Office365IntegrationAdapterTestData


class Office365GatherTest(AvaCoreTest):
    def setUp(self):
        pass
        # # Make call to super.
        # super(Office365GatherHistoryTest, self).setUp()
        #
        # # Set the data type.
        # self.data = Office365GatherHistoryTestData()

    def test_office365_gather_import(self):
        self.assertEqual(1, "Test not written")


# Implementation
class Office365GatherHistoryTest(AvaCoreTest):
    # step 2: replace appName and Office365GatherHistory
    model_name = 'gather_office365.Office365GatherHistory'

    has_owner = False

    # step 3: populate this section to define what you expect the API permissions will be
    api_permissions = {
        'create': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
        'retrieve': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
        'update': {'unauthenticated': False, 'standard': False, 'admin': False, 'owner': False},
        'delete': {'unauthenticated': False, 'standard': False, 'admin': False, 'owner': False},
    }

    # step 4: update with the model name for apiviewset urls (for apiviews and custom api's this won't work
    api_urls = {
        'create': 'office365gatherhistory-list',
        'retrieve': 'office365gatherhistory-detail',
        'retrieve_all': 'office365gatherhistory-list',
        'update': 'office365gatherhistory-detail',
        'delete': 'office365gatherhistory-detail',
    }

    def setUp(self):
        # step 5: Update with Model Names
        super(Office365GatherHistoryTest, self).setUp()
        self.data = Office365GatherHistoryTestData()

    def create_object_via_api(self, data, user='admin'):
        # step 6: you will need to write this method.... this template only works with single models
        # with no relationships

        # This model requires a valid integration object

        url = reverse("office365-setup-list")
        integration = Office365IntegrationAdapterTestData()

        if user:
            # must be admin to create
            self.login_user(user=user)
        else:
            self.logout_user()

        response = self.client.post(url, integration.standard, format='json')
        # print("Response :: " + str(response.data))

        # return the id of the model you are testing
        if 'id' in response.data:
            data['integration'] = response.data['id']

            url = reverse(self.api_urls['create'])

            if user:
                # must be admin to create
                self.login_user(user=user)
            else:
                self.logout_user()
                user = 'unauthenticated'

            # print("Data :: " + str(data))
            response = self.client.post(url, data, format='json')
            # print("Response :: " + str(response.data))
            self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                                   permitted=self.api_permissions['create'][user])

            self.logout_user()

            # return the id of the model you are testing
            if 'id' in response.data:
                return response.data['id']
        else:
            self.assertIn(response.status_code, self.status_forbidden)

    # step 7: replace office365gatherhistory globally with your model name in lowercase
    def test_office365gatherhistory_create_as_user(self):
        self.create_object_via_api(data=self.data.standard, user='standard')

    def test_office365gatherhistory_create_as_admin(self):
        self.create_object_via_api(data=self.data.standard, user='admin')

    def test_office365gatherhistory_create_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard, user=None)

    def test_office365gatherhistory_retrieve_single_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_office365gatherhistory_retrieve_all_as_user(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_office365gatherhistory_retrieve_single_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_office365gatherhistory_retrieve_all_as_admin(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_office365gatherhistory_retrieve_single_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_office365gatherhistory_retrieve_all_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_office365gatherhistory_update_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_office365gatherhistory_update_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_office365gatherhistory_update_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['admin'])

    def test_office365gatherhistory_update_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['admin'])

    def test_office365gatherhistory_update_exists_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_office365gatherhistory_update_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_office365gatherhistory_delete_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_office365gatherhistory_delete_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_office365gatherhistory_delete_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['admin'])

    def test_office365gatherhistory_delete_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['admin'])

    def test_office365gatherhistory_delete_exists_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])

    def test_office365gatherhistory_delete_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])
