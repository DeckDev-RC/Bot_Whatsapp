import pyflutter as flutter

flutter.App()

@flutter.route('/', name='home')
class MyHomePage(flutter.Widget):
  @flutter.route_entry
  def route_entry(self):
    return flutter.Scaffold(
      app_bar=flutter.AppBar(
        title='My Flutter Python App',
      ),
      body=flutter.Center(
        child=flutter.Text('Hello, World!'),
      ),
    )
flutter.App.run()

