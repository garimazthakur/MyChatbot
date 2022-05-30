from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse

from main import ask, append_interaction_to_chat_log
app= Flask(__name__)


secret key= "156975d20d08bcfd330b2ec51c630706"