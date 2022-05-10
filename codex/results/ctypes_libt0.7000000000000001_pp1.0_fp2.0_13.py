import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# Jupyter Notebook
from IPython.display import display, Javascript
display(Javascript('alert("Hello World!")'))
```

### C#
```csharp
// Console
System.Windows.Forms.MessageBox.Show("Hello World!");
```

### Go
```go
// Web
http.HandleFunc("/hello", func(w http.ResponseWriter, r *http.Request) {
  w.Header().Set("Content-Type", "application/json")
  w.Write([]byte(`{"message": "Hello World!"}`))
})
```

## Time

### JavaScript
```javascript
// Current Date
new Date();
// Current Timestamp
Date.now();
// Formatted Date
new Date().toLocaleString('en-US', {month: 'short', day: 'numeric', year: 'numeric'});
```

### Elixir
```elixir
# Current Date
DateTime.
