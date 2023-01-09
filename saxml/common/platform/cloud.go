// Copyright 2022 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Package cloud registers a Cloud environment.
package cloud

import (
	"time"

	"saxml/common/platform/cloudenv"
	"saxml/common/platform/env"
)

func init() {
	env.Register(new(cloudenv.Env))
}

// SetOptionsForTesting updates watchPeriod so that during tests, file changes are detected sooner.
func SetOptionsForTesting(watch time.Duration) {
	cloudenv.SetOptionsForTesting(watch)
}
