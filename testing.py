import convertapi

"""convertapi.api_secret = 'iw7Ryzu4trL8gA3x'
result=convertapi.convert('txt', {
    'File': 'dummy.pdf'
})
"""

convertapi.api_secret = 'iw7Ryzu4trL8gA3x'
convertapi.convert('txt', {
    'File': 'dummy.pdf'
}, from_format = 'pdf').save_files('/notes')