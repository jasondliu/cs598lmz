import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(sys.argv[1:]))).start()
```

### Jest

```js
// jest.config.js
module.exports = {
  runner: 'jest-runner-script',
  displayName: 'script',
  testMatch: ['<rootDir>/src/**/*.js']
};
```

### Karma

```js
// karma.conf.js
module.exports = function(config) {
  config.set({
    files: ['src/**/*.js'],
    frameworks: ['script'],
    plugins: ['karma-script-launcher'],
    reporters: ['progress'],
    port: 9876,
    colors: true,
    logLevel: config.LOG_INFO,
    autoWatch: true,
    singleRun: false,
    concurrency: Infinity,
    browsers: ['ChromeHeadless']
  });
};
```

### Mocha

```js
// mocha.opts
--require script-laun
