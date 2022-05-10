import sys, threading

def run():
    while True:
        line = sys.stdin.readline()
        if line == '':
            break
        print(line.strip())

threading.Thread(target=run).start()
</code>
I have tried to do the same in a react app but it doesn't work
<code>import React from "react";
import StartServer from "./StartServer";
import { render, fireEvent, waitForElement } from "@testing-library/react";
import "@testing-library/jest-dom/extend-expect";

jest.mock("child_process");

describe("StartServer", () =&gt; {
  it("Should show the server output", async () =&gt; {
    const { getByText } = render(&lt;StartServer /&gt;);
    fireEvent.click(getByText(/start/i));

    await waitForElement(() =&gt; getByText(/server started/i));
  });
});
</code>
The test does not work as it doesn't expect anything from the server. How can I
