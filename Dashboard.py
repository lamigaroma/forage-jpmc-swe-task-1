import perspective

# Create a Perspective Table
data = {"name": ["Alice", "Bob", "Charlie"], "age": [25, 30, 35]}
table = perspective.Table(data)

# Create a Perspective View
view = table.view()

# Start Perspective WebSocket Server
server = perspective.PerspectiveServer()
server.add_table("my_table", table)
server.start()

# Open Perspective Viewer in a Web Browser
viewer_url = server.host + "/#table=my_table"
print(f"Open the viewer at: {viewer_url}")

# Keep the script running to maintain the server
server.join()