let socket_global = null

function get_socket() {
  if (socket_global){
    return socket_global
  } else {
    socket_global = io()
    return socket_global
  }  
}

function submit() {
  let socket = get_socket()
  let chat_input = document.getElementById("chat_input")
  let responses = document.getElementById("responses")
  let message = chat_input.value
  chat_input.value = ""
  
  let bubble = document.createElement("p")
  bubble.className = "user_message"
  bubble.setHTML(message)
  responses.append(bubble)
  socket.emit("message", {data: message})
}

function enter(event) {
  if (event.key != "Enter") {return}
  submit()
}

function response(text) {
  let bubble = document.createElement("p")
  bubble.className = "response_message"
  let responses = document.getElementById("responses")
  bubble.setHTML(text)
  responses.append(bubble)
}
