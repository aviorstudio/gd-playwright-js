<!-- Generated from private documentation source. Do not edit directly. Source SHA256: aec1a30f29c4e7f9afe937c5916a61d40fa8ac8c06e3b7a876a34a708f5ebf4c -->

# gd-playwright JavaScript helpers

MIT-licensed Playwright helpers for Godot web games. The Godot addon is [gd-playwright](https://github.com/aviorstudio/gd-playwright); its Rust companion lives in [gd-playwright-cli](https://github.com/aviorstudio/gd-playwright-cli).

## Install

Install the source package from this repository, pinned to a reviewed commit:

```sh
npm install git+https://github.com/aviorstudio/gd-playwright-js.git#COMMIT
```

The package name remains `@aviorstudio/gd-playwright`. The library accepts an existing Playwright `page` and adds no runtime dependencies.

## Usage

```js
import { clickElement, dragElement, resolveElement, waitForGodotEvent } from "@aviorstudio/gd-playwright";

await clickElement(page, "start_button", { confirm: "route_loaded" });
await dragElement(page, "card_1", { toKey: "board_slot_2", retries: 2 });
```

The diagnostic game export exposes `window.godotElements`, viewport metadata and `godot-event` events through the addon. Helpers resolve current positions immediately before input, account for canvas scaling, arm confirmation listeners before input and release the mouse after failed actions. Games control which diagnostic data they expose.

## Development

Run `mise run check` for syntax validation, Bun behavior tests, package creation and actual packed-module export verification. `mise run build` writes the npm tarball under `dist/`; `mise run clean` removes generated package output.

## License and provenance

MIT. `SOURCE.json` records the original public source revision and file hashes.
