/**
 * Register jest-dom matchers (toBeInTheDocument, ...) on Vitest 5 assertions.
 *
 * @testing-library/jest-dom still augments the Vitest <=4 `Assertion<T>` interface,
 * which no longer matches Vitest 5's `Assertion<R, T>`. Vitest 5 exposes a
 * dedicated `Matchers<R, T>` interface for custom matchers, so we extend it here.
 * Runtime registration stays in ./setup.ts (`import '@testing-library/jest-dom'`).
 */
import type { TestingLibraryMatchers } from '@testing-library/jest-dom/matchers';

declare module 'vitest' {
  // eslint-disable-next-line @typescript-eslint/no-empty-object-type, @typescript-eslint/no-unused-vars
  interface Matchers<R extends void | Promise<void> = void | Promise<void>, T = unknown>
    extends TestingLibraryMatchers<unknown, R> {}
}
