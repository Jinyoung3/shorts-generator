Purpose: Turn the LLM into an agent.

This file:

loads prompt + state + tools

sends context to the LLM

interprets the response

decides:

call a tool

stop and output