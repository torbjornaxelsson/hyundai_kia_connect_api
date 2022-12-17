import logging
import time
from hyundai_kia_connect_api import *
import asyncio
logging.basicConfig(level=logging.DEBUG)

async def test():
  max_count = range(5)
  interval = 10

  vm = VehicleManager(region=2, brand=2, username="dasheroni2012@gmail.com", password="Pro.2021", pin="4523")
  await vm.check_and_refresh_token()
  transaction_id = await vm.lock('w7IC5uYOqg6PfXln2bt98Q==')
  
  for count in range(max_count):
    _LOGGER.debug(f"Last action check: waiting {interval} seconds")
    await asyncio.sleep(interval)
    _LOGGER.debug(f"Last action check: attempt {count} of {max_count}")
    is_completed = await self.hass.async_add_executor_job(
        self.vehicle_manager.check_action_status, vehicle_id, action_id
    )
    if is_completed:
      _LOGGER.debug(f"Last action check: was completed")
      return True
  _LOGGER.debug(f"Last action check: action did not complete")
  return False



asyncio.run(test())


	#result = vm.api.check_last_action_status(vm.token, vm.get_vehicle('w7IC5uYOqg6PfXln2bt98Q=='), transaction_id)

#climate_request_options = ClimateRequestOptions(
#    #duration=call.data.get("duration"),
#    set_temp=23,
#    climate=1,
#    heating=1,
#    defrost=1,
#)
#
#transaction_id = vm.start_climate('w7IC5uYOqg6PfXln2bt98Q==', climate_request_options)

#transaction_id = vm.lock('w7IC5uYOqg6PfXln2bt98Q==')

#print(transaction_id)
#transaction_id = vm.start_climate('w7IC5uYOqg6PfXln2bt98Q==', climate_request_options)

#time.sleep(10)
#result = vm.api.check_last_action_status(vm.token, vm.get_vehicle('w7IC5uYOqg6PfXln2bt98Q=='), transaction_id)
#print(result)
#time.sleep(10)
#result = vm.api.check_last_action_status(vm.token, vm.get_vehicle('w7IC5uYOqg6PfXln2bt98Q=='), transaction_id)
#print(result)
#time.sleep(10)
#result = vm.api.check_last_action_status(vm.token, vm.get_vehicle('w7IC5uYOqg6PfXln2bt98Q=='), transaction_id)
#print(result)
#

#vm.force_refresh_vehicle_state(vm.get_vehicle('w7IC5uYOqg6PfXln2bt98Q=='))