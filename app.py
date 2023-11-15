import streamlit as st
import asyncio
from nyc_data_pipeline.source_extract_async import NYCPublicDataFetcher, NYCEndpointFetcher
import os
import json

def run_async(func):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(func)

def fetch_and_save_data(query):
    async def fetch_data():
        data_fetcher = NYCPublicDataFetcher(query)
        data = await data_fetcher.run()
        endpoint_fetcher = NYCEndpointFetcher()
        endpoints_dict = await endpoint_fetcher.run(data)
        return endpoints_dict

    data = run_async(fetch_data())
    if data:
        if not os.path.exists('data'):
            os.makedirs('data')
        with open('data/data.json', 'w') as file:
            json.dump(data, file)
        st.write(f'Data saved to data/data.json')
    else:
        st.write('No data fetched')


st.title('NYC Open Data Fetcher')
query = st.text_input('Enter your query:')
if st.button('Fetch and Save Data'):
    fetch_and_save_data(query)
