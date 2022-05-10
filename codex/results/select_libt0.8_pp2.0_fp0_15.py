import selector from './selector';

describe('selector', () => {
  const state = {
    app: {
      countries: [
        {
          name: 'Russia',
          population: 146580740,
          capital: 'Moscow',
          currencies: [
            {
              code: 'RUB',
              name: 'Russian ruble',
              symbol: '₽',
            },
          ],
          flag: 'https://restcountries.eu/data/rus.svg',
        },
        {
          name: 'USA',
          population: 323947000,
          capital: 'Washington, D.C.',
          currencies: [
            {
              code: 'USD',
              name: 'United States dollar',
              symbol: '$',
            },
          ],
          flag: 'https://restcountries.eu/data/usa.svg',
        },
        {
          name: 'Japan',
          population: 126451398,
          capital: 'Tokyo',
          currencies: [
            {
              code: 'JPY
